"""
Simplified Nikola plugin to generate LLM-friendly markdown versions.
Creates /llms.txt and corresponding .md files for articles.
"""

import os
import re
import glob
from pathlib import Path
from nikola.plugin_categories import Task
from nikola import utils


class GenerateLLMsText(Task):
    """Generate LLM-friendly markdown versions of articles."""

    name = "generate_llms_txt"

    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        return super().set_site(site)

    def gen_tasks(self):
        """Generate tasks to create LLMs.txt and related files."""
        self.logger = utils.get_logger('generate_llms_txt', utils.STDERR_HANDLER)
        self.kw = {
            "output_folder": self.site.config["OUTPUT_FOLDER"],
            "index_file": self.site.config["INDEX_FILE"],
            "default_lang": self.site.config["DEFAULT_LANG"],
        }

        yield self.group_task()

        # Directly get all markdown files from the articles directory
        article_files = glob.glob('articles/*.md')
        self.logger.info(f"Found {len(article_files)} markdown files in articles directory")

        # Generate llms.txt root index
        yield {
            'basename': self.name,
            'name': 'llms_txt_index',
            'targets': [os.path.join(self.kw['output_folder'], 'llms.txt')],
            'actions': [(self.create_root_index, [article_files])],
            'uptodate': [utils.config_changed(self.kw)],
            'clean': True,
        }

        # Generate individual .md files for each article
        for article_path in article_files:
            # Get the base filename without extension
            article_basename = os.path.splitext(os.path.basename(article_path))[0]
            # Create the target .md file path in the output directory
            md_target = os.path.join(self.kw['output_folder'], f"{article_basename}.md")

            yield {
                'basename': self.name,
                'name': f'llms_md_{article_basename}',
                'targets': [md_target],
                'actions': [(self.create_md_file, [article_path, md_target])],
                'uptodate': [utils.config_changed(self.kw)],
                'clean': True,
            }

    def create_root_index(self, article_files):
        """Create the root /llms.txt index file."""
        output_path = os.path.join(self.kw['output_folder'], 'llms.txt')
        site_name = self.site.config.get('SITE_NAME', 'Documentation Site')

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w') as f:
            f.write(f"# {site_name} - LLM-Friendly Documentation\n\n")
            f.write(f"This is the machine-readable documentation index for {site_name}.\n\n")

            f.write("## All Articles\n\n")

            # Sort articles alphabetically
            for article_path in sorted(article_files):
                # Get the base filename without extension
                article_basename = os.path.splitext(os.path.basename(article_path))[0]

                # Get post object from Nikola
                post = self.get_post_by_source_path(article_path)
                if post and post.title():
                    title = post.title()
                else:
                    # Fall back to filename if post not found or no title
                    title = article_basename.replace('_', ' ')

                # Create a link to the .md file
                f.write(f"- [{title}](/{article_basename}.md)\n")

        self.logger.info(f"Created llms.txt index at {output_path}")
        return True

    def get_post_by_source_path(self, source_path):
        """Get the Nikola post object for a given source file path."""
        # Convert to absolute path if needed
        source_path = os.path.abspath(source_path)

        # Iterate through all posts to find the matching one
        for post in self.site.timeline:
            if os.path.abspath(post.source_path) == source_path:
                return post

        # Try pages too, since articles are likely pages
        for page in self.site.pages:
            if os.path.abspath(page.source_path) == source_path:
                return page

        return None

    def create_md_file(self, source_path, target_path):
        """Create an individual .md file."""
        try:
            # Get original markdown content
            with open(source_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Process content - fix internal links
            content = self.process_markdown_links(content)

            # Write the processed markdown
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(content)

            self.logger.info(f"Created LLM markdown file at {target_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error creating MD file for {source_path}: {e}")
            return False

    def process_markdown_links(self, content):
        """Process markdown content to update internal links."""
        # Update internal links to point to .md versions
        # Match markdown links [text](url)
        link_pattern = r'\[(.*?)\]\(((?!http|\:\/\/).*?)(\.html)?\)'

        def replace_link(match):
            text = match.group(1)
            url = match.group(2)

            # Extract the base path without extension
            base_url = url.rstrip('/')
            if base_url.endswith('.html'):
                base_url = base_url[:-5]  # Remove .html
            elif base_url.endswith('/index'):
                base_url = base_url[:-6]  # Remove /index

            # Convert to .md link
            return f'[{text}]({base_url}.md)'

        # Replace links in content
        processed_content = re.sub(link_pattern, replace_link, content)
        return processed_content
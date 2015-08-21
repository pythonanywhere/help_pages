# help_pages
The help pages for help.pythonanywhere.com

When they're ready to go, add this to the www.pythonanywhere.com block in the
load balancer's nginx config:

    location /wiki/ {
        rewrite ^/wiki/(.*) http://help.pythonanywhere.com/pages/$1 permanent;
    }


To get feedback working, we'll also need to csrf_exempt feedback.views.submit and
add response["Access-Control-Allow-Origin"] = "http://help.pythonanywhere.com"
to the response when the request comes from help.pythonanywhere.com
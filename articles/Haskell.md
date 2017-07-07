
<!--
.. title: Haskell
.. slug: Haskell
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




PythonAnywhere already comes with the Haskell ghc already installed. For example, you could do `runhaskell your-haskell-file.hs` to compile and run your own Haskell file. [Here](//learnyouahaskell.com/) is a great intro to Haskell.

Once you have gotten more familiar with Haskell, you may find that you want to setup automatic testing etc for your project. Below is a sample workflow to set up a Cabal environment where you can build your package and run tests:

    :::bash
    # setup ~/.cabal and download latest package list from hackage.haskell.org
    cabal update

    # upgrade cabal-install, the CLI tool, to a shiny new version to get sandbox functionality
    cabal install cabal-install --jobs=5

    # the newly updated cabal will live in ~/.cabal/bin/cabal; make sure you are using it
    echo "alias cabal=~/.cabal/bin/cabal" >> ~/.bashrc && source ~/.bashrc

    mkdir a-cool-haskell-project
    cd a-cool-haskell-project

    # setup a "virtualenv"
    cabal sandbox init
    # create your cabal package!
    cabal init



After you have all this set up, you will be able to start developing your cabal package! Some common commands include:

    :::bash
    # after you making changes, rebuild and run test suite
    cabal build && cabal test --test-options="colors" --show-details="always"

    # if there are new build dependencies that you added to your .cabal file, need to configure and install packages before you build
    cabal configure --enable-tests && cabal install --only-dependencies --enable-tests --jobs=5



You may also find [these](//www.stephendiehl.com/what/) [articles](//mambo.cab/how-to-make-a-thing-in-haskell-3) interesting and informative. Also, [hspec](//hspec.github.io/) has a useful automatic test discovery thing that may be pretty useful.

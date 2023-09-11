#! /usr/bin/env zsh

hugo && rsync -r public/* swizzard@ssh.hcoop.net:public_html

The main config file is `.rehome.json`

Here is example config:

```json
{
    "shell": "zsh",
    "checks": {
        "which zsh": "apt-get install zsh",
        "which vim": "apt-get install vim",
        "which tmux": "apt-get install tmux"
    },
    "repos": {
        ".vim/bundle/Vundle.vim": "VundleVim/Vundle.vim",
        "src/quotes": "git@github.com:hiqsol/quotes"
    },
    "installs": {
        "bin/composer": [
            "wget https://getcomposer.org/installer -O composer-setup.php",
            "php composer-setup.php --install-dir=bin --filename=composer",
            "rm composer-setup.php"
        ]
    },
    "updates": {
        "bin/composer": [
            "bin/composer self-update"
        ],
        "prj/hiqdev/hidev/vendor": [
            "cd prj/hiqdev/hidev/vendor ; composer update"
        ]
    }
}
```

Looks quite clear:

- `shell` - given shell will be set with `chsh`
- `checks` - runs given commands and notifies on fails with given comments
- `repos` - given repos will be installed/updated to given paths
- `installs` - given scripts will be run to install paths if they don't exist
- `updates` - given scripts will be run to update paths


# btbatw.org website

## Local build instructions

### Install dependencies

```bash
gem install jekyll bundler
bundle install
```

### Run development server

```bash
bundle exec jekyll serve
```

### Build files for publication

```bash
bundle exec jekyll build
```

### Add twitter bootstrap 4
Refer to [this](https://simpleit.rocks/how-to-add-bootstrap-4-to-jekyll-the-right-way/#fnref:safe-mode)

### Site structure reference
[Github on demand training](https://github.com/github/training-kit)

## Local build instructions for M1 Mac:

### Install rails first:

```bash
sudo gem install rails
```

### install jekyll

```bash
sudo gem install jekyll bundler
```

### Make jekyll executable by the following tricks

```bash
sudo gem uninstall sassc
gem install sassc --user-install
gem install --user-install sassc -- --disable-march-tune-native

sudo arch -x86_64 gem install ffi
brew install gpg2
gpg2 --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
\curl -sSL https://get.rvm.io | bash -s stable --rails
rvm use 3
sudo gem install jekyll bundler

cd /Path/To/Your/Sites/
arch -x86_64 jekyll new BTBA
cd /Path/To/Your/Sites/BTBA

bundle install
bundle add webrick
bundle update
```

### Clone the repo and serve

```bash
git clone https://github.com/btbatw/www.btbatw.org.git
cd www.btbatw.org
bundle exec jekyll serve
```

The site will be served at `http://127.0.0.1:4000/`

## Add static symposium site as git submodule

```bash
# git submodule add -b [branchname] [git url] [destination local directory]
git submodule add -b website https://github.com/btbatw/symposium-2022.git ./2022/

# for local repo freshedly cloned and has submodule
git submodule update --init 
```

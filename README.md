# Markdown book skeleton
Skeleton files for writing a book using markdown. Typora is recommended

Copy the book-example folder to book

## How-to

```
mkdir my-new-awesome-book
git clone https://github.com/epiecs/markdown-pandoc-book-template.git .
cp -r book-example/ book
cd book
```

Then initialize your seperate git repo in the book folder. Be sure to check and modify `meta.yml` and `pandoc.yml`

## Folders

- All chapters are in the `book/chapters` folder.
- All front matter (thanks etc) is in the `book/front_matter folder
- All back matter (appendix etc) is in the `book/back_matter folder
    - All back matter content will have no chapter numbering but will be included in the toc

## Usage

You need make to use this skeleton. Use `make book` to build the entire book. This wil render a pdf, epub, html and docx version of your book. Everything will be put in the `build` folder.

The difference between the print and web pdf is that the print pfd includes extra blank pages to make sure that a new chapter starts on an uneven page

## Make commands

`make environment` installs all programs

`make markdown` combines all chapters and runs script to build 1 markdown file

`make <epub|html|pdf-web|pdf-print|docx>` generate a specific format

`make book` and `make all` generates all formats

`make pdf` generates web and print pdf's

`make clean` verwijdert de gegenereerde files

Be sure to check out the makefile to tweak everything to your needs

## Book and pandoc settings

All book settings can be found in `meta.yaml`
All pandoc settings can be found in `pandoc.yaml`

## Includes

If make gives you trouble just run make clean first.

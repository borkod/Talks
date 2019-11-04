## **INTRODUCTION**
## **TO**
## **MARKDOWN**

NOTES:
_[1 minutes]_

- Thank the organizers and the audience

=====

### Agenda

* What is Markdown?
* Why use Markdown?
* Markdown Syntax
* Markdown Tools
* Markdown Resources

=====

### What is Markdown?
<p align="left">
* [Wikipedia](https://en.wikipedia.org/wiki/Markdown) defines Markdown as:
> Markdown is a lightweight markup language with plain text formatting syntax.
</p>
* Markdown is one of the world’s most popular markup languages


NOTES:
_[2 minutes]_

- Using Markdown is different than using a WYSIWYG editor.
- In an application like Microsoft Word, you click buttons to format words and phrases, and the changes are visible immediately.
- Markdown isn’t like that. When you create a Markdown-formatted file, you add Markdown syntax to the text to indicate which words and phrases should look different.

=====

### Why use Markdown?

Here we'll have a link:

[Some Link](https://www.b3o.ca)

NOTES:
_[2 minutes]_

- Promises have been in browser and Node for 2 years, yet I think there still seems to be this aversion or at least lack of will to adopt them and use them.
- Bluebird and Q still popular Promise libraries, which just leads to fragmantation, which will only cause problems in future
- Express still order of magnitude more popular than Koa, the Promise-based spiritual successor to Express.
- This is due partly to technical reasons. Node core API is callback-based because maps nicely to underlying v8 platform, and so since it's the root API that everyone has to use, the paradigm carries through into the user land.
- But Promise-based Node will come eventually.
- Similarly `XHR` and ajax is event / callback based, and `fetch()` adoption lagging
- Technical and comminity issues

=====

### Markdown Syntax
#### Headings

|Syntax|Alternate|Result|
|------|---------|------|
|`# Heading 1`|Heading 1<br>=========|<h1>Heading 1</h1>|

NOTES:
_[2 minutes]_

=====

### Markdown Syntax
#### Headings

|Syntax|Alternate|Result|
|------|---------|------|
|`## Heading 2`|Heading 2<br>------------|<h2>Heading 2</h2>|
|`### Heading 3`|   |<h3>Heading 3</h3>|

=====

### Markdown Syntax
#### Ephasis

|Syntax|Alternate|Result|
|------|---------|------|
|`*Italic*`|`_Italic_`|*Italic*|
|`**Bold**`|`__Bold__`|**Bold**|
|`***Italic and Bold***`|`___Italic and Bold___`|***Italic and Bold***|
|`~~Strikethrough~~`|   |~~Strikethrough~~|

=====

### Markdown Syntax
#### Ordered Lists

<br>`1. 1st ordered list item`
<br>`2. 2nd ordered list item`
_____
1. 1st ordered list item
2. 2nd ordered list item

=====

### Markdown Syntax
#### Unordered Lists

<br>`* List item`
<br>`- List item`
<br>`+ List item`
_____
* List item
- List item
+ List item

=====

### Markdown Syntax
#### Links

|Syntax|Result|
|------|------|
|`[Link](http://www.edc.ca)`|[Link](http://www.edc.ca)|
|`![Image](https://www.edc.ca/content/dam/edc/EDC-logo.svg)`|![Image](https://www.edc.ca/content/dam/edc/EDC-logo.svg)|

=====

## Markdown Syntax
#### Blockquotes

`> The highest forms of understanding we can achieve are laughter and human compassion.`
_____
> The highest forms of understanding we can achieve are laughter and human compassion.

=====

## Markdown Syntax
#### Code Blocks
<p align="left">
`` ``` ``
<br>print "Hello World!"
<br>`` ``` ``
</p>
_____
```
print "Hello World!"
```

=====

### Markdown Resources
#### Editors

<p align="left">
There are many Markdown editors offering features such as:
</p>
- Syntax highlight and auto-complete
- Side by side previews

<p align="left">Couple of popular options:
</p>
- [Typora](https://typora.io/)
- [Visual Studio Code](https://code.visualstudio.com/)

=====

### Markdown Resources
#### Online Editors

<p align="left">
There are also many online editors available that work right in your browser!
<br>
<br>Few options:
</p>
- [StackEdit](https://stackedit.io/)
- [Dillinger](https://dillinger.io/)
- [Markdown Editor](https://jbt.github.io/markdown-editor/)
  
=====

### Markdown Resources
#### Links

- [An introduction to Markdown](https://opensource.com/article/19/9/introduction-markdown)
- [Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Another Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Markdown Tutorial](https://www.markdowntutorial.com/)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [The 10 Best Markdown Editors](https://www.shopify.ca/partners/blog/10-of-the-best-markdown-editors)

NOTES:
_[2 minutes]_

=====
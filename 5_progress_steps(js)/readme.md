# Boilerplates

Make three files:

1. index.html
2. style.css
3. script.js

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"
      integrity="sha512-z3gLpd7yknf1YoNbCzqRKc4qyor8gaKU1qmn+CShxbuBusANI9QpRohGBreCFkKxLhei6S9CQXFEbbKuqLg0DA=="
      crossorigin="anonymous"
      referrerpolicy="no-referrer"
    />
    <title>Document</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <script src="script.js"></script>
  </body>
</html>
```

> In the `head` tag, I added the link to the `style.css` file and the link to the `font awesome`.
> In the `body` tag, I added the `script` tag to the `script.js` file.
> I added a `h1` tag with the text `hello world` in the `body` tag.

now open the file with live server and u will see the hello world text.

Now edit the `style.css` file and add this code:

```css
@import url("https://fonts.googleapis.com/css2?family=Mooli&family=Roboto:ital,wght@0,400;1,100&display=swap");

* {
  box-sizing: border-box;
}

body {
  font-family: "Roboto", sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  overflow: hidden;
  margin: 0;
}
```

> I imported the `Roboto` font from google fonts.
> I added the `box-sizing: border-box;` to all the elements. You can learn more about `box-sizing` [here](https://www.w3schools.com/css/css3_box-sizing.asp#:~:text=The%20box%2Dsizing%20property%20allows,are%20the%20same%20size%20now!).

> I added the `font-family: 'Roboto', sans-serif;` to the `body` tag. If `Roboto` font is not available, the browser will use the `sans-serif` font.

Lets break down the `body` tag:

- when you open the html file with live server, the `body` tag will take the whole page and `hello world` text will be in the middle of the page.

- its because:
  - `display: flex;` will make the `body` tag a flex container. flex container will give you the ability to use flex properties on the children elements. like `justify-content`, `align-items`, `flex-direction`, etc.
  - `flex-direction: column;` will make the flex container a column. so the children elements will be in a column.
  - `align-items: center;` will center the children elements horizontally.
  - `justify-content: center;` will center the children elements vertically. But you won't see the effect of this property becuse the `body` tag will take the whole page. So, you have to add `height` to the `body` tag to see the effect of this property.
  - `height: 100vh;` will make the `body` tag take the whole page vertically. `vh` means viewport height. `100vh` means 100% of the viewport height.
  - `overflow: hidden;` will hide the scroll bar.
  - `margin: 0;` will remove the default margin of the `body` tag.

u shoould use these properties in a chronological order. if you change the order, you will get a different result.
Try it urself.

# Progress Steps


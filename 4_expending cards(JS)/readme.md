I downloaded the 50 day 50 project course from Udemy to improve my CSS and JS skills and I am going to try to do all of them. I will be using HTML, CSS, and JavaScript.

So, this is the first One

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

# Expending Cards

Make a new folder and copy the `html`,`css`,`JS` boilerplates files into it.

Open the `index.html` and we can start writting the code.

> remove the `hello world` text from the `body` tag and change the `title` tag to `Expending Cards`.

we need to make a div where the `images` will show in the background. so, add this code to the `body` tag:

```html
<body>
  <div class="container">
    <div
      class="panel active"
      style="
          background-image: url('https://www.planetware.com/wpimages/2020/02/france-in-pictures-beautiful-places-to-photograph-eiffel-tower.jpg');
        "
    >
      <h3>Explore the world</h3>
    </div>
  </div>
  <script src="script.js"></script>
</body>
```

> I added a `div` tag with a class of `container` and a `div` tag with a class of `panel active` inside it.

Now copy the `div` with the class of `panel active` and paste it 4 times. so, you will have 5 `div` tags with a class of `panel active`.

> remove the `active` class from all `div` tag, exepct the first one.

We, made our html template. Lets style it.

Open the `style.css` file and add this code:

```css
...
body {
    font-family: 'Roboto', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    overflow: hidden;
    margin: 0;
}
...
```

> I removed the `flex-direction: column;` from the `body` tag.

Evething is the same except the `flex-direction: column;`. We removed it because we want the `div` tags to be in a row.

```css
...
body {
    font-family: 'Roboto', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    overflow: hidden;
    margin: 0;
}

.container {
    display: flex;
    width: 90vw;
}
...
```

> I added the `display: flex;` to the `container` class. so, the `div` tags will be in a row.

> I added the `width: 90vw;` to the `container` class. so, the `div` tags will take 90% of the viewport width.

This will make the `div class="panels"` to be in a row. but, they will be on top of each other. so, we need to add `position: relative;` to the `container` class.

```css
.panel {
    /* background-size: auto; can be used to make the image fit the panel */
    /* background-size: auto 100%; can be used to make the image fit the panel and keep the aspect ratio */
    background-size: auto 100%; 
    background-position: center;
    background-repeat: no-repeat;
    height: 80vh;
    border-radius: 50px;
    cursor: pointer; /* to change the cursor to a pointer when hovering over the panel */
    color: seashell;
    flex: .5 ; 
    /*to make the panels take up half the width of the container */
    margin: 10px;
    position: relative; /* to position the h3 element and relative to the panel */
    transition: flex 0.7s ease-in-out; /* to make the transition smooth */
}
```

> I added the `background-size: auto 100%;` to the `panel` class. so, the image will fit the panel and keep the aspect ratio.

> I added the `background-position: center;` to the `panel` class. so, the image will be in the center of the panel.

> I added the `background-repeat: no-repeat;` to the `panel` class. so, the image will not repeat.

> I added the `height: 80vh;` to the `panel` class. so, the panels will take 80% of the viewport height.

> I added the `border-radius: 50px;` to the `panel` class. so, the panels will have a border radius of 50px.

> I added the `cursor: pointer;` to the `panel` class. so, the cursor will change to a pointer when hovering over the panel.

> I added the `color: seashell;` to the `panel` class. so, the text color will be seashell.

> I added the `flex: .5 ;` to the `panel` class. so, the panels will take up half the width of the container.

> I added the `margin: 10px;` to the `panel` class. so, the panels will have a margin of 10px.

> I added the `position: relative;` to the `panel` class. so, the `h3` element will be relative to the panel.

> I added the `transition: flex 0.7s ease-in-out;` to the `panel` class. so, the transition will be smooth.

```css
.panel h3 {
    font-size: 24px;
    position: absolute;
    bottom: 20px;
    left: 20px;
    margin: 0;
    opacity: 0;
}
```

> I added the `font-size: 24px;` to the `panel h3` class. so, the font size will be 24px.

> I added the `position: absolute;` to the `panel h3` class. so, the `h3` element will be absolute to the panel.

> I added the `bottom: 20px;` to the `panel h3` class. so, the `h3` element will be 20px from the bottom.

> I added the `left: 20px;` to the `panel h3` class. so, the `h3` element will be 20px from the left.

> I added the `margin: 0;` to the `panel h3` class. so, the `h3` element will have a margin of 0.

> I added the `opacity: 0;` to the `panel h3` class. so, the `h3` element will have an opacity of 0.

```css
.panel.active {
    flex: 5;
}

.panel.active h3 {
    opacity: 1;
    transition: opacity 0.3s ease-in 0.4s;
}
```

> I added the `flex: 5;` to the `panel active` class. so, the active panel will take up 5 times the width of the other panels.

`panel active h3` class is the same as `panel h3` class except the `opacity` and `transition` properties.

> I added the `opacity: 1;` to the `panel active h3` class. so, the `h3` element will have an opacity of 1.

To make the page responsive, we need to add a media query.

```css
@media (max-width: 480px) {
    .container {
        width: 100vw;
    }

    .panel:nth-of-type(4),
    .panel:nth-of-type(5) {
        display: none;
    }
}
```

> I added the `@media (max-width: 480px)` to the `style.css` file. so, the styles inside the media query will be applied when the viewport width is less than 480px.

when the viewport width is less than 480px, the `container` class will take 100% of the viewport width. and the 4th and 5th `panel` will not be displayed. 

Now if u look at the page, u will see the panels. but, when u click on a panel, nothing will happen. so, we need to add some JavaScript.

Open the `script.js` file and add this code:

```js
const panels = document.querySelectorAll(".panel");

panels.forEach((panel) => {
  panel.addEventListener("click", () => {
    panel.classList.add("active");
  });
});
```

> I selected all the elements with a class of `panel` and stored them in a variable called `panels`.

> I looped through the `panels` variable and added a `click` event listener to each panel.

> when a panel is clicked, the `active` class will be added to the panel.

This will make the panel take 5 times the width of the other panels. but, when u click on another panel, the `active` class will be added to it so it will take 5 times the width of the other panels. so, we need to remove the `active` class from the other panels or we will face some problems like the other panel will still take 5 times the width of the other panels.

```js
const panels = document.querySelectorAll(".panel");

panels.forEach((panel) => {
  panel.addEventListener("click", () => {
    removeActiveClasses(); // to remove the active class from the other panels
    panel.classList.add("active");
  });
});


// to remove the active class from the other panels
function removeActiveClasses() {
    panels.forEach(panel => {
        panel.classList.remove("active");
    });
}
```

> I created a function called `removeActiveClasses` to remove the `active` class from the other panels.

> I called the `removeActiveClasses` function before adding the `active` class to the panel.

Now, if u click on a panel, the `active` class will be added to it and the `active` class will be removed from the other panels.

Now, if u click on a panel, the `active` class will be added to it and the `active` class will be removed from the other panels. 

AND  that it for the Expending Cards project.

we made a responsive Expending Cards project using HTML, CSS, and JavaScript. I know expending cards is not a big project but it is a good project to practice your HTML, CSS, and JavaScript skills. 

I hope you found this helpful.
## v-on description

### basic usage
```html
<button v-on:click="btnclick"></button>
```

### @click.stop
```markdown
To prevent event bubbling.
```
```html
<button @click.stop="btnclick"></button>
```


### prevent 
To prevent auto-submit of form.
```html
<form action="">
<button @click.prevent="submitclick"></button>
</form>
```

### keyup
```markdown
To listen event when we lift our finger on the keyboard
```
```html
<input type="text" @keyup.enter="keyup">
```

### click for one time 
```markdown 
Invoke the function only when the first time user click the button
```
```html
<button @click.once="once"></button>
```

## v-if|v-else-if|v-else



## v-show
```
Similar as v-if ,but v-show add a style="display:None"
when the tag changes quickly and frequently, use v-show, use v-if when changes just once.
```

## v-for 
```
traverse
```
```html
<ul>
    <li v-for="item in names">{{item}}</li>
    <!-- when traverse an object in javascript, we get the value every time --> 
    <!-- when traverse a python dict object,we get the key   -->
    <li v-for="(value,key,index) in names">{{value}}--{{key}}--{{idnex}}</li>
    <!-- javascript object is ordered  -->
</ul>
```

## javascript splice()
+ remove elements
```javascript
array = [1,2,3,4]
array.slice(1,2)
```

+ insert elements 
```javascript
array = [1,2,3,4]
```


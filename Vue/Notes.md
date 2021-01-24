# VUE

## Javascript 
+ var | let | const
```html
<script>
    // static variable
    const app = new Vue({})
    // dynamic variable 
    // changeble
    let app = new Vue({})
    // var is not recommend in es6.
</script>
```
+ loops
```javascript
books = ["呵呵","哈哈","嘻嘻"]
for (let i=0;i<=books.length;i++){
    console.log(books[i])
}
for (let i in books){
    console.log(books[i])
}
for (let i of books){
    console.log(i)
}
```
+ closure
```html
<script>
buttons = document.getElementByTagName("button");
for (var i=0;i<buttons.length;i++;){
    (function(index){
        buttons[index].addEventListener("click",function(){
            console.log("第" + index + "个按钮被点击了");
        });
    })(i)
}
</script>
```
```html
<script>
buttons = document.getElementByTagName("button");
for (let i=0;i<buttons.length;i++;){
    console.log("第" + index + "个按钮被点击了");
}
</script>
```

## Vue:basic vue
```html
<div id="app">{{message}}</div>
<script src=""></script>
<script>
    const app = new Vue({
        el:"#app", // manage label element
        data:{
            message:"Hello,world"
        }
    })
</script>

```

## Vue:show list
```markdown
D:\SkillsAndKnowledge\Vue\VueShowList.html
```


## Vue:counter
```markdown
D:\SkillsAndKnowledge\Vue\VueCounter.html
```


## Basic tags elements
```html
<div v-mustache="message"></div>
<script src=""></script>
<script>
    const app = new Vue({
        el:"#app", // manage label element
        data:{
            message:"Hello,world"
        }
    })
</script>
```

## v-bind
+ keyword:
```markdown 
v-bind:class=
v-bind:style=

abbrveation
:class=
:stle=
```
```markdown
Vue_v-bindclass.html

Vue_v-bindstyle.html
```

## computed 计算属性
+ computed attribute contains cache
```javascript
<div id="app">
    {{fullName}}
</div>
<script>
        const obj = {
            firstName: "Kobe",
            lastName: "bryant"
        }
        const app = new Vue({
            el: "#app",
            data: obj,
            computed: {
                fullName: function () {
                    return this.firstName + this.lastName
                }
            }
        })
</script>
```

## Simplify attributes
```javascript
<script>
const app = new Vue({
  el:"#app",
  firstName: "Kobe",
  lastName: "bryant",
  methods: {
    fullName(){
      return this.firstName + this.lastName
    }
  }
})
</script>
```

## v-on 
+ basic script
```html
<button v-on:click>+</button>
<button v-on:click>-</button>

<!--sugar-->
<button @click="increment">+</button>
<button @click="decrement">-</button><!--omit the () when where are no args -->
```
+ with args
```html
<button @click="click"> </button>
<script>
const app = new Vue({
  el:"#app",
  methods: {
    click(event){
      console.log(event);
    }
  }
})
</script>
```
```html
<button @click="click(123,$event)"></button>
<!--Here 123 is a basic data type if we pass 'abc' as an argument, vue will search variable abc in app  -->
<script>
  const app = new Vue({
    el:"#app",
    methods: {
      click(arg,event){
          console.log(arg);
          console.log(event);
      }
    }
  })

</script>
```


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

## js 响应式 与非响应式
+ 响应式
```markdown
1. array.push()
2. array.pop()
3. array.shift()
4. array.unshift()
5. array.splice()
6. 
```
+ 非响应式
```markdown
1. 通过数组改变值

```
## javascript splice()
+ remove elements
```javascript
array = [1,2,3,4]
// splice(start_index,count(default:all))
array.splice(1,2)
```
+ update elements 
```javascript
array = [1,2,3,4]
array.splice(1,3,"m","n","k")
```
+ add elements
```javascript
array=[1,2,3,4]
array.splice(1,0,"c","d")
```


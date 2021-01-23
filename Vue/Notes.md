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
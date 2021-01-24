const app = new Vue({
  el: "#app",
  data: {
    books: [
    {
      id: 1,
      name: "<算法导论>",
      publishedDate: "2006-9",
      price: 85,
      count: 1
    },
    {
      id: 2,
      name: "<UNIX编程艺术>",
      publishedDate: "2006-2",
      price: 59,
      count: 1
    },
    {
      id: 3,
      name: "<编程珠玑>",
      publishedDate: "2008-10",
      price: 39,
      count: 1
    },
    {
      id: 4,
      name: "<代码大全>",
      publishedDate: "2006-3",
      price: 128,
      count: 1
    }]
  },
  methods: {
    increment(index) {
      this.books[index].count++;
    },
    decrement(index) {
      this.books[index].count--;
    },
    del(index) {
      this.books.splice(index, 1);
    }
  },
  computed: {
    totalPrice() {
      let total = 0
      for (let i of this.books) {
        total += i.price*i.count
      }
      return total
    }
  },
  filters: {
    priceStyle(price) {
      return "￥" + price.toFixed(2)
    }
  }
})
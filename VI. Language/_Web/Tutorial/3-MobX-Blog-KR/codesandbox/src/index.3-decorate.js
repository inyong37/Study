import { 
  observable, 
  reaction, 
  computed, 
  autorun, 
  decorate, 
  action, 
  transaction 
} from "mobx";

class GS25 {
  basket = [];

  get total() {
    console.log("calculating...");
    return this.basket.reduce((prev, curr) => prev + curr.price, 0);
  }

  select(name, price) {
    this.basket.push({ name, price });
  }
}

decorate(GS25, {
  basket: observable,
  total: computed,
  select: action
});

const gs25 = new GS25();
autorun(() => gs25.total);
autorun(() => {
  if (gs25.basket.length > 0) {
    console.log(gs25.basket[gs25.basket.length - 1]);
  }
});
gs25.select("water", 800);
console.log(gs25.total);
gs25.select("water", 800);
console.log(gs25.total);
gs25.select("chips", 1500);
console.log(gs25.total);

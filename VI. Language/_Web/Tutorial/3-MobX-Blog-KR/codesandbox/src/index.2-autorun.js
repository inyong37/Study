import { observable, reaction, computed, autorun } from "mobx";

const calculator = observable({
  a: 1,
  b: 2
});

const sum = computed(() => {
  console.log("calculating...");
  return calculator.a + calculator.b;
});

autorun(() => console.log(`a value has changed to ${calculator.a}!`));
autorun(() => console.log(`b value has changed to ${calculator.b}!`));
autorun(() => sum.get());

sum.observe(() => calculator.a);
sum.observe(() => calculator.b);

console.log(sum.value);

calculator.a = 10;
calculator.b = 20;

console.log(sum.value);

calculator.a = 50;

console.log(sum.value);

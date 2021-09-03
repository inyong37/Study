// https://velog.io/@velopert/MobX-1-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-9sjltans3p

import { observable, reaction, computed, autorun } from "mobx";

const calculator = observable({
  a: 1,
  b: 2
});

reaction(
  () => calculator.a,
  (value, reaction) => {
    console.log(`a value has changed to ${value}!`);
  }
);

reaction(
  () => calculator.b,
  (value) => {
    console.log(`b value has changed to ${value}!`);
  }
);

const sum = computed(() => {
  console.log("calculating...");
  return calculator.a + calculator.b;
});

sum.observe(() => calculator.a);
sum.observe(() => calculator.b);

console.log(sum.value);

calculator.a = 10;
calculator.b = 20;

console.log(sum.value);

calculator.a = 50;

console.log(sum.value);

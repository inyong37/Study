// https://velog.io/@velopert/MobX-2-%EB%A6%AC%EC%95%A1%ED%8A%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EC%97%90%EC%84%9C-MobX-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-oejltas52z
// https://velog.io/@velopert/MobX-3-%EC%8B%AC%ED%99%94%EC%A0%81%EC%9D%B8-%EC%82%AC%EC%9A%A9-%EB%B0%8F-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%B0%A9%EB%B2%95-tnjltay61n

import React from 'react';
import ReactDOM from 'react-dom';
import  { Porvider } from 'mobx-react';
import App from './App';
import CounterStore from './stores/counter';
import MarketStore from './stores/market'

const counter = new CounterStore();
const market = new MarketStore();

ReactDOM.render(
  <Provider counter={counter}, market={market}>
    <App />
  </Porivder>
  document.getElementById('root')
);

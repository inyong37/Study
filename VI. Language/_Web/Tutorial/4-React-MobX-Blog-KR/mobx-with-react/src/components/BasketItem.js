import React from 'react';
import './BasketItem.css';
import { observer } from 'mobx-react';

const BasketItem = ({ name, price, count, onTake }) => {
	return (
		<div className="BasketItem">
			<div className="name">{name}</div>
			<div className="price">{price}원</div>
			<div className="count">{count}</div>
			<div className="return" onClick={() => onTake(name}>갖다놓기</div>
		</div>
	);
};

export default observer(BasketItem);
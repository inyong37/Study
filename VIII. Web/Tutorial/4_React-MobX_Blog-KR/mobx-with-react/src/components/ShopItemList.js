import React from 'react';
import ShopItem from './ShopItem';
import { inject, observer } from 'mobx-react';

const items = [
	{
		name: '생수',
		price: 850,
	},
	{
		name: '신라면',
		price: 900,
	},
	{
		name: '포카칩',
		price: 1500,
	},
	{
		name: '새우깡',
		price: 1000,
	},
];

const ShopItemList = ({ onPut }) => {
	const itemList = items.map(item => (
		<ShopItem {...item} key={item.name} onPut={onPut} />
	));
	return <div>{itemList}</div>;
};

export default inject(({ market }) => ({
	onPut: market.put,
}))(observer(ShopItemList));
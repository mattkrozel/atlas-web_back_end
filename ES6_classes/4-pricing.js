export default class Pricing {
  constructor(amount, currency) {
    this._ammount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._ammount;
  }

  get currency() {
    return this._currency;
  }

  set currency(n) {
    this._currency = n;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}

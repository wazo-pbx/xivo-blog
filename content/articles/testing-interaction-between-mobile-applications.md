Title: Testing Interactions Between Mobile Applications: A Bumpy Ride
Date: 2019-02-22 13:14:00
Author: Emmanuel QUENTIN
Category: Wazo IPBX
Tags: Mobile, testing
Slug: testing-interaction-between-mobile-applications
Status: published

# Testing Interactions Between Mobile Applications: A Bumpy Ride

![callkeep](https://user-images.githubusercontent.com/2076632/52963046-ca98b200-336c-11e9-8c82-590c0bed8839.gif)

For the past couple weeks, we've been working on how to automate integration tests on our mobile application. This application is built with react-native and uses edge technologies like native WebRTC, native UI with ConnectionService or CallKit (see our library [callkeep](https://github.com/wazo-pbx/react-native-callkeep)) and wake up push notification.

Avoiding regression on a large application like this seems to be a huge challenge, but we're making big steps in the automation process.

## You Must Choose, but Choose Wisely

The first step of our journey was the choose a testing framework that will fit our needs. Software like Selenium or Appium have proven they value, but they're also slow and flaky. At the end of our investigation, we've selected [Detox](https://github.com/wix/Detox) to run our tests. Detox generates less flaky tests, because it monitors the app waiting for interaction or requests to finish before moving to the next instruction.

## A Telephony App: We Need More Power

Testing interaction on a single application is pretty straightforward: tap on button and see what happens. But what if we have to test interactions between multiple devices ?
Detox doesn't document how to run 2 devices and check how to interact. So we need to dig a little bit.

## Starting Another Device

To launch another device, we need another instance of `Detox`, and call `launchApp` on it `device` attribute:
```js
// Takes configuration from package.json (our test are ran with `yarn e2e:test:ios` or `yarn e2e:test:android` so can we check the environment variable `npm_lifecycle_event`)
const deviceConfig = require('../package.json').detox.configurations[process.env.npm_lifecycle_event === 'e2e:test:ios' ? 'ios.sim.debug' : 'android.emu.debug']; 
const otherDetox = new Detox({ deviceConfig });
await otherDetox.device.launchApp();

const { expect: otherExpect, by: otherBy, element: otherElement } = otherDetox.device.deviceDriver.expect;
// Do something with `otherExpect`, `otherBy`, and `otherElement` to handle checks on the other device
```

Success ! Another device is launched, but wait, why all other actions target the new device and not the first one ?!

## There Are 2 Hard Problems in Computer Science...

And caching is one of them !

After a lot of hair pulling, we found that Detox uses a simple variable in a module to store the [`invocationManager`](https://github.com/wix/Detox/blob/a8e4bc0469e8ebb9be68bc863ecceb1166de704d/detox/src/ios/expect.js#L23) in the `expect.js` module. A little later in the code, this module is required and the [invocation manager is set](https://github.com/wix/Detox/blob/a8e4bc0469e8ebb9be68bc863ecceb1166de704d/detox/src/devices/drivers/IosDriver.js#L15-L16).

And what happens when we create another instance of `Detox` ? The [nodejs require cache](https://nodejs.org/api/modules.html#modules_caching) doesn't require the `expect.js` module again and the `invocationManager` is overridden when `IosDriver` calls `setInvocationManager`. As a result, our 2 instances of `detox` use the same `invocationManager`: the last one. That's why interactions occur only on the last device started.

## Avoiding the Require Cache, Round 1

A first try to avoid nodejs caching the `invocationManager` was to wrap the module in a method:
```js
module.exports = function() {
	let invocationManager;
	function setInvocationManager(im) {
	  invocationManager = im;
	}

	// ...
	return { /**/	};
}
```
And then in the caller:
```diff
+ const configureExpect = require('../../ios/expect');
// ...

- this.expect = require('../../ios/expect');
+ this.expect = configureExpect();
```

This way, the `invocationManager` would be cached for each call of `configureExpect`.

This method works this way, but the mock of the module in the unit test would be very complicated, because we'd have to mock every method of the module. That's because Jest doesn't know about all return attributes in our wrapper. 

## Avoiding the Require Cache, Round 2

Another way to avoid this cache is to make a class of the module, set the `invocationManager` as an attribute and instantiate it like :
```diff
+ const IosExpect = require('../../ios/expect');
// ...
- this.expect = require('../../ios/expect');
- this.expect.setInvocationManager(new InvocationManager(this.client));
+ this.expect = new IosExpect(new InvocationManager(this.client));	
```

Jest is also aware of each methods of our class and can mock them automatically !

## Success !

After some research and some failure, we are now able to test interactions between multiple devices with Detox easily !

We've made a [PR of our journey](https://github.com/wix/Detox/pull/1144). You can +1 it if you want to done the same on your application !

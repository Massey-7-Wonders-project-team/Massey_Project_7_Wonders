# Cross Browser Support


## Browsers
We have tested our application on Internet Explorer 11, Microsoft Edge (latest), Google Chrome (latest), Mozilla Firefox (latest), Apple Safari (latest), Android Chrome (latest), Apple Safari for iOS (latest)

### Babel Polyfill
This allows us to use some of the native Javascript methods that are implemented on newer browsers, but has a polyfill for browser which don't support it. This includes methods such as Object.assign()


### Fetch
We use the browser api `fetch` for most of our calls to our api server. Fetch is not compatible on some older browsers such as IE, so we use import the package `isomorphic-fetch` as a polyfill. We also import the `es6-promise` polyfill as `fetch` is actually a promise under the hood.

### Tap events on iPhones
To avoid the 300ms delay on Safari we use the react-tap-event-plugin and use onTouchTap instead of onClick

More info here on [react-tap-event-plugin](https://github.com/zilverline/react-tap-event-plugin)

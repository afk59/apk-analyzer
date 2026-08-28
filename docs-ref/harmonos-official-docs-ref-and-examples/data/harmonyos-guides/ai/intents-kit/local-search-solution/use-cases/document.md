# Use Cases

#### Typical Scenarios

**Function search**: By integrating your in-app functions with Intents Kit, you enable users to directly access these functions via Celia Search. Users can simply search for the relevant function name or app name. For example, if a map app has integrated the "Member Center" function with Intents Kit, a user searching for either the app name or "Member Center" can find this specific function and, upon tapping, be directly taken to that function page within the app.

**Content search**: Take music as an example. While a user is interacting with a music app, the app can use its client-side API to share music data with Intents Kit. This data could include songs the user has already listened to or even songs the app predicts the user might be interested in. Later, when the user searches for a song title in Celia Search, the system will look for matching content within the data the app has shared and display the results using a template widget. When a user taps the interactive area of the widget, they can either jump directly to the music playback page or trigger playback in the background.

#### Widget Display Effect

Intents Kit provides standard template widgets that can be displayed in Celia Search for each vertical domain. You do not need to develop the widgets yourself.

The template widgets contain necessary information about the app or atomic service and content, such as the song name, cover, and description. You need to share these parameters with the system. The widget styles vary across vertical domains, depending on the specific requirements of the actual functions and scenarios.

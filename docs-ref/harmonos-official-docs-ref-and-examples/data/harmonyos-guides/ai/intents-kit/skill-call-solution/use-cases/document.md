# Use Cases

Users interact with Celia Chat through natural language input to obtain their desired services and retrieve content. The primary scenarios fall into two categories: task execution and one-step access to functions. Task execution includes two subtypes: by triggering functional services and through information interaction.

1.  Task execution:
    -   Functional services: Calling a device-side intent will directly redirect a user to the corresponding function page within the app or atomic service, with business parameters passed as needed.
    -   Information interaction: Calling a cloud-side or device-side intent will perform content searches and display the results. Users can then tap the displayed information on their device to complete the intent call process.
2.  One-step access to functions: Calling a device-side intent will instantly redirect users to the corresponding function page within the app, without requiring additional parameters. You can configure multiple functions for direct access in batches.

#### Typical Scenarios

## Functional Services

-   The page that users are redirected to does not contain parameters: For example, to query transaction details, users can say "Query transaction details of the XX bank card". Then the corresponding app landing page will be displayed.
-   The page that users are redirected to contains parameters: For example, to hail a taxi using the XX app, users can say "Use XX to hail a taxi to XX Mall". Users will be redirected to the taxi booking page and the extracted destination address will be automatically filled in.
-   The function is executed and a windowed UI is displayed: For example, to control the Bluetooth switch, users can say "Enable Bluetooth". Then the Bluetooth setting window will pop up and the Bluetooth switch will be turned on.

## Information Interaction

-   Content display scenario: For example, to search for a recipe, users can say "How to make a sandwich".
-   Function fulfillment scenario: For example, to book a movie ticket, users can say "Buy two tickets for today's movie xxx". Then they can proceed with purchasing and selecting seats for the movie.

## One-Step Access to Functions

After in-app functions are registered with Intents Kit, Celia allows users to directly open specific function pages. For instance, saying "Open HUAWEI Video's membership center" will trigger the corresponding page without additional steps.

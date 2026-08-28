# Restrictions on the Number of Live Views

1\. ID restrictions for live view creation: Multiple live views can be created at a time, each with a unique ID. Only one live view with a specific ID can exist concurrently. (After the live view with a specific ID ends, Live View Kit can use this ID to create a new live view immediately, but Push Kit cannot create a new live view using this ID within 12 hours.)

2\. Interaction restrictions for live view display: Up to 24 live views can be displayed by sliding in the notification panel. The live view list displayed by tapping a capsule can contain only a maximum of five live views and cannot be slid.

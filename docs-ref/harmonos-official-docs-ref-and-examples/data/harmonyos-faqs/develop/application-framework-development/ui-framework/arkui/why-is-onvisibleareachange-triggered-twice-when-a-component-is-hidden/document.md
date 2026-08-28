# Why is onVisibleAreaChange triggered twice when a component is hidden?

**Symptom**

With **ratios** set to **\[0, 1\]**, a component's disappearance triggers the **onVisibleAreaChange** event twice.

**Solution**

To trigger the event only once, set only one ratio.

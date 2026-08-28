# What should I do if the constraintSize settings fail to take effect?

**Symptom**

If **constraintSize** is set for a component and the width of its child component is set to a percentage, for example, **width('100%')**, **constraintSize** takes effect by multiplying the maximum width by the percentage. As a result, the child component may overflow, in which case it looks like the **constraintSize** settings fail to take effect.

**Solution**

You can use the **Scroll** component at the outer layer. In this way, when **constraintSize** is set and the space occupied by a child component exceeds the specified constraint value, a scrollbar will be displayed.

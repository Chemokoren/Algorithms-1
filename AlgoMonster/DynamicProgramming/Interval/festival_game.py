"""
Festival Game | Bursting Balloons

It's finally here, the annual Umbristan fall festival! Everyone in Umbristan gets a few extra days off work to go celebrate the festival. You and your co-workers decide to go out to the festival with your extra time off. At this festival there are various game you can play to collect points which you can redeem for prizes. One game catches your eye which is a shooting game. You shoot a pellet gun at a series of targets lined up where each target has a value. Whenever you hit a target you gain points equal to the target's value multiplied by the target values both to the left and to the right of the hit target that has not been hit yet. If we represent the target values as a linear array, then we say when you hit target[i], you gain target[i - 1] * target[i] * target[i + 1] in points. You being the sharpshooter that you are know you can hit with 100% accuracy but you don't know the maximal points you can get from this game. Can you figure out the maximum number of points that can be gained from this game?

If you are on the edge of the targets then simply multiply by 1 instead.

The number of targets will not exceed 400.

The value on each target is in the range 1 <= value <= 500

The answer is guaranteed to fit in an integer
Examples:
Example 1:
Input: target = [1, 5]
Output: 10
Explanation:

Shoot target 1 which gets you 1 * 5 * 1 = 5 points then target 2 which get you 1 * 5 * 1 = 5 points.
Example 2:
Input: target = [1, 5, 4]
Output: 30
Explanation:

Shoot targets 3, 1, 2 in that order.
"""
# UI Specification

This document defines how to document user interface specifications for the project.

## Page Documentation Format

Each page/screen should be documented with the following structure:

```markdown
## [Page Name]

### Purpose
Brief description of what this page does and its role in the user flow.

### Route
`/path/to/page`

### Layout
- Header: [description]
- Main content: [description]
- Sidebar (if any): [description]

### Components Used
- ComponentA
- ComponentB

### States
- Loading: [description]
- Empty: [description]
- Error: [description]
- Success: [description]

### Actions
| Action | Trigger | Result |
| --- | --- | --- |
| Submit form | Click button | API call, redirect |

### Responsive Behavior
- Mobile: [changes]
- Tablet: [changes]
- Desktop: [default]
```

## Component State Documentation

Document all possible states for interactive components:

| State | Visual | Behavior |
| --- | --- | --- |
| Default | Normal appearance | Awaiting interaction |
| Hover | Subtle color change | Cursor pointer |
| Active/Pressed | Darker shade | Visual feedback |
| Focus | Focus ring visible | Keyboard accessible |
| Disabled | Muted colors, 50% opacity | No interaction |
| Loading | Spinner or skeleton | Prevents re-submission |
| Error | Red border/text | Shows error message |

## Responsive Breakpoints

Design mobile-first. Document breakpoint-specific changes:

| Breakpoint | Width | Layout Changes |
| --- | --- | --- |
| Mobile | < 640px | Single column, stacked elements |
| Tablet | 640px - 1023px | Two columns, collapsed nav |
| Desktop | ≥ 1024px | Full layout, sidebar visible |

## Accessibility Checklist

For each page/component, verify:

- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Color is not the only indicator
- [ ] Keyboard navigation works
- [ ] Focus order is logical
- [ ] Screen reader announces correctly

## Wireframe Conventions

When creating wireframes:

- Use grayscale to focus on layout
- Annotate interactive elements
- Show all states (especially empty/error)
- Include responsive versions

---

## Pages

> **Note:** Document each page below as it is designed.

_No pages documented yet._

# Data and dashboards

Use when people monitor, compare, investigate, or act on structured information. Identify the decision a view supports before changing its density. A professional operations table may need many simultaneous values; hiding columns or enlarging cards can increase task effort. Read [evaluation and metrics](../foundations/evaluation-and-metrics.md) to choose evidence tied to the decision.

## Preserve information meaning

Expose scope, units, time range, timezone, update time, and relevant missing-data meaning. Distinguish zero from unavailable, not applicable, or not yet measured. An average without its population or time window can mislead even when visual hierarchy is excellent. Align numeric columns, label units, and make formatting consistent with [content and localization](../foundations/content-and-localization.md).

Choose a table for exact lookup and cross-row comparison, a chart for a relationship or trend, and a summary for a known high-level question. A chart should have an accessible route to its important information; an equivalent table or concise description must preserve meaning rather than merely list decorative colors. Avoid requiring hover to reveal essential values.

For the web, a static table and an interactive grid are different interaction contracts. Native HTML tables are appropriate for tabular reading; APG's grid pattern introduces managed keyboard navigation and composite-widget responsibilities. Sorting or links inside a table do not automatically require a grid role. [APG table guidance](https://www.w3.org/WAI/ARIA/apg/patterns/table/) and [APG grid guidance](https://www.w3.org/WAI/ARIA/apg/patterns/grid/).

## Keep exploration stable

Make active filters visible, explain combined conditions where necessary, and offer targeted clearing. Indicate sort direction and sorting field. Preserve selection by stable record identity rather than row position; updates and sorting must not silently select another item. Bulk actions should state their scope, especially when some records are hidden by filters or pagination.

```text
view = { filters, sort, page_or_cursor, selected_record_ids }
data = { records, received_at, source_status }
refresh: reconcile records without changing selection identity
```

For rapidly updating datasets, decide whether rows may reorder automatically while someone is reading or acting. Freeze ordering during interaction, provide a controlled refresh, or offer another task-appropriate stable view. If displaying stale data is preferable to an empty screen, label freshness and the failed update. Never use a live-looking animation to imply a feed is healthy.

Virtualization can reduce rendering cost, but introduces focus, offscreen content, and accessibility concerns. Test real navigation with the selected component and assistive technology. Avoid claiming complete dataset access merely because the visible rows work. If the task needs comprehensive export or searching, verify those operations include the intended records.

Use [cognitive load](../principles/cognitive-load.md) and [working memory](../principles/working-memory.md) to reduce repeated mental joins: keep comparison context nearby and make selected records inspectable. [Hick's Law](../principles/hick-law.md) supports organizing action choices. [Jakob's Law](../principles/jakob-law.md) supports familiar table behaviors. None requires reducing expert density to a novice card layout.

## Example and counterexample

A service dashboard identifies "Response time, milliseconds, last 30 minutes", keeps the last successful sample during reconnect, and marks it stale. Clicking a point filters the incident table; Back restores the prior interval. Counterexample: a green "Healthy" tile survives a disconnected feed, missing samples become zero, and reordering rows causes a bulk action to affect different servers.

## Acceptance checks

- Perform exact lookup, comparison, and investigation tasks using realistic row counts and missing values.
- Verify filter, selection, sorting, detail-return, and bulk-action scope after refresh and pagination.
- Check chart information without hover or color discrimination, and tables with keyboard and target assistive technology.
- Test disconnected feeds, partial data, extreme values, empty datasets, and updates during action selection.
- Measure task errors and interpretation accuracy alongside rendering performance. Preserve justified expert density.

Sources consulted: 2026-10-04. APG supplies informative web semantics and interaction guidance; numeric accessibility requirements live in [accessibility](../foundations/accessibility.md). Freshness and identity models are skill recommendations.

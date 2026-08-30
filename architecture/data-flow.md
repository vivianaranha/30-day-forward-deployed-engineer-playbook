# Data Flow

1. User enters ticket information.
2. UI sends it to `/analyze`.
3. API validates input.
4. Business logic derives category and priority.
5. AI layer produces summary and recommendation explanation.
6. Integration layer can persist the result.
7. Metrics are recorded.
8. UI presents the recommendation.

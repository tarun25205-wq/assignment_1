/*
  Step 1: Start the algorithm
*/
START

/*
  Step 2: Input number of shelves and clothes details
  n → number of shelves
  clothes → list containing category and usage frequency
*/
READ n
READ clothes_list

/*
  Step 3: Categorize clothes based on type
  Example: Formal, Casual, Traditional, Party
*/
GROUP clothes_list BY category

/*
  Step 4: Assign priority based on frequency of use
  High    → Daily wear
  Medium  → Weekly wear
  Low     → Occasional wear
*/
ASSIGN priority TO each category

/*
  Step 5: Allocate shelves according to priority
  Middle shelves → High priority clothes
  Lower shelves  → Medium priority clothes
  Upper shelves  → Low priority clothes
*/
ALLOCATE shelves BASED ON priority

/*
  Step 6: Arrange clothes within each shelf
  - Fold clothes neatly
  - Keep similar clothes together
  - Place frequently used clothes in front
*/
ARRANGE clothes IN shelves

/*
  Step 7: Label each shelf with category name
  This helps reduce searching time
*/
LABEL shelves

/*
  Step 8: End the algorithm
*/
END
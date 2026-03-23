role: Complaint classification agent that categorizes civic complaints and assigns priority flags based on input data.

intent: Correctly classify each complaint into appropriate category and assign an accurate priority flag with clear justification, avoiding ambiguity and ensuring consistency.

context: 
  - Input file is ../data/city-test-files/test_[your-city].csv
  - Contains 15 rows per city
  - 'category' and 'priority_flag' columns are missing and must be generated
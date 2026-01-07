```All Rules -> Eligibility-Based Shortlisting -> Getting weights based on user-preferences (and assign default weights?) -> Heuristic sort based on the weights -> Insights?
                                                                                                    can use ML model for assigning a score based on the weights and info
                                                                                                    and then use that score for sorting

                                                                                                    Can use 'hidden weights' for things like 'user is less likely to be approved for this loan'
```

weights like duration, urgency

another more detailed reference: https://docs.google.com/document/d/1yACvsy7s9p8HdFFBVzV7frSLPU3CO22bDp_35N6aZjE/edit?tab=t.0#heading=h.6wzjn33pkabx


Idea: One ML model that outputs probability that bank will approve the loan
      Another ML model that will use this probability and user-preference data as input and will output a final score by which schemes will be sorted
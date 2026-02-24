# Tableau Calculated Fields (Examples)

**Retention %**
```
IF [cohort_users] = 0 THEN 0
ELSE [active_users] / [cohort_users]
END
```

**Cohort Week Label**
```
DATENAME('year', [cohort_week]) + '-' + RIGHT('0' + STR(DATEPART('week',[cohort_week])), 2)
```

**Sessions per User**
```
IF [dau] = 0 THEN 0
ELSE [sessions] / [dau]
END
```

SELECT B.BuildingName, ISNULL(Count, 0) as 'Count'
FROM Buildings B
LEFT JOIN (SELECT A.BuildingID, COUNT(*) as 'Count'
    FROM Apartments A
    INNER JOIN Requests R
    ON A.AptID = R.AptID 
    AND R.Status = 'Open'
    GROUP BY A.BuildingID) Req_Counts
WHERE B.BuildingID = Req_Counts.BuildingID
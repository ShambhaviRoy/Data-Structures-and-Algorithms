SELECT TenantName
FROM Tenants
INNER JOIN (SELECT TenantID
    FROM AptTenants
    HAVING COUNT(*) > 1) TC
ON TC.TenantID = Tenants.TenantID
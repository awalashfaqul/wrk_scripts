request = function()
  wrk.method = "PUT"
  wrk.body = '{"number": 2, "number_of_seats": 6, "is_available": false}'
  wrk.headers["Content-Type"] = "application/json"
  return wrk.format(nil, "/api/tables/5e0b8f4-1c2d-4a3b-9c5f-7a2d6e5f3b8") -- Replace with real UUID
end

done = function(summary, latency, requests)
  local file = io.open("latency_log_dotnet_put.csv", "w")
  file:write("Metric,Value\n")
  file:write(string.format("Average,%.2f\n", latency.mean / 1e6))
  file:write("Percentile,Latency_ms\n")
  for _, p in ipairs({50, 75, 90, 95, 99, 99.9}) do
    file:write(string.format("%.1f,%.2f\n", p, latency:percentile(p) / 1e6))
  end
  file:close()
end
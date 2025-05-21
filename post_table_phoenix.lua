local latencies = {}

request = function()
  wrk.method = "POST"
  wrk.body = '{"number": 1, "number_of_seats": 4, "is_available": true}'
  wrk.headers["Content-Type"] = "application/json"
  return wrk.format(nil)
end

done = function(summary, latency, requests)
  local file = io.open("latency_log_dotnet_post.csv", "w")
  file:write("Metric,Value\n")
  file:write(string.format("Average,%.2f\n", latency.mean / 1e6))
  file:write("Percentile,Latency_ms\n")
  for _, p in ipairs({50, 75, 90, 95, 99, 99.9}) do
    file:write(string.format("%.1f,%.2f\n", p, latency:percentile(p) / 1e6))
  end
  file:close()
end
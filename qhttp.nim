import std/httpclient
import nimpy
import std/tables
import std/json
    
type PyHttpResponse = ref object of PyNimObjectExperimental
  content*: string
  status*: string
  headers*: TableRef[string, seq[string]]
  version*: string

proc json(self: PyHttpResponse): JsonNode {.exportpy.} = 
  return parseJson(self.content)

proc newPyHttpResponse(resp: Response): PyHttpResponse = 
  return PyHttpResponse(content: resp.body(), status: resp.status, headers: resp.headers.table, version: resp.version)
proc get(url: string): PyHttpResponse {.exportpy.} = 
  var client = newHttpClient()

  let output = newPyHttpResponse(client.get(url))
  return output
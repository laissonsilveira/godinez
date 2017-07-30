export default class IssueController {
  constructor (http) {
    this.http = http;
  }
  findAll (callback) {
    this.http.get("http://localhost:5000/issues").then((response) => {
      console.log("calling findAll");
      callback(response.data);
    })
  }
}

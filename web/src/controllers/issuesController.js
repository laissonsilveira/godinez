export default class IssueController {

  constructor (http) {
    // jogar para uma variavel global
    this.url = "http://localhost:5000/issues";
    this.http = http;
  }

  findAll (callback) {
    this.http.get(this.url).then((response) => {
      callback(response.data);
    });
  }

  save (issue, callback) {
    this.http.post(this.url, issue).then((response) => {
      callback && callback();
    });
  }

}

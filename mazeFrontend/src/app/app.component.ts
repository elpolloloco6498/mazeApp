import { Component } from '@angular/core';

let API_ENDPOINT = "http://localhost:5000"

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Maze App';
  formData = {
    "width": 10,
    "height": 10,
    "solution": false
  };
  mazeData:any

  handleUpdateForm($event:any) {
    this.formData = $event;
    console.log(this.formData)
  }

  async handleSubmit() {
    console.log("Form submitted!")
    this.mazeData = await this.generateMaze()
    console.log(this.mazeData)
  }

  generateMaze() {
    var raw = JSON.stringify({
      "width": this.formData.width,
      "height": this.formData.height
    });
    console.log(raw)
    return fetch(API_ENDPOINT, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: raw
      })
      .then(response => response.json())
      .then(result => {
        return result
      })
      .catch(error => console.log('error', error));
  }
}

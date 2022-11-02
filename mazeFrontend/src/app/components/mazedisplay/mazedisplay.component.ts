import { Component, OnInit, Input, SimpleChange} from '@angular/core';
import * as d3 from "d3";
import { mazeData } from 'src/app/mocks/mazeMock';
//let cells = mazeData["cells"] MOCK

let colorCell = 'white';
let colorPath = "red";
let colorEntry = "green";
let colorExit = "black";
let canvasWidth = 800;
let canvasHeight = 800;
let w = 100;
let h = 100;


@Component({
  selector: 'app-mazedisplay',
  templateUrl: './mazedisplay.component.html',
  styleUrls: ['./mazedisplay.component.css']
})
export class MazedisplayComponent implements OnInit {
  @Input() dataMaze:any;
  @Input() solution:any;
  private svg:any;
  constructor() { }

  ngOnInit(): void {
    console.log(this.dataMaze)
    this.svg = d3.select("#canvas").attr("width", canvasWidth).attr("height", canvasHeight)
  }

  ngOnChanges(changes: SimpleChange) {
    this.drawMaze()
  }

  clearCanvas() {
    this.svg.selectAll("*").remove();
  }

  drawSolution(w:number, h:number) {
    for (let cell of this.dataMaze.solve) {
      this.drawCell(cell, colorPath, w, h)
    }
  }

  drawCell(cell:any, color:string, w:number, h:number) {
    let x = cell.i*w;
    let y = cell.j*h;
    // draw rectangle
    this.svg.append("rect")
    .attr("x", function(cell:any){ return x })
    .attr("y", function(cell:any){ return y })
    .attr('width', w)
    .attr('height', h)
    .attr('fill', color)

    // draw walls
    let walls = cell.walls
    if (walls.N) {
      this.drawLine(x, y, x+w, y)
    }
    if (walls.W) {
      this.drawLine(x, y, x, y+h)
    }
    if (walls.S) {
      this.drawLine(x, y+h, x+w, y+h)
    }
    if (walls.E) {
      this.drawLine(x+w, y, x+w, y+h)
    }
  }

  drawLine(x1:number, y1:number, x2:number, y2:number) {
    this.svg.append('line')
    .style("stroke", "black")
    .style("stroke-width", 5)
    .attr("x1", x1)
    .attr("y1", y1)
    .attr("x2", x2)
    .attr("y2", y2);
  }

  drawMaze() {
    if (this.dataMaze) {
      //compute w and h cell dimensions
      let w = Math.floor(canvasWidth/this.dataMaze.cols);
      let h = Math.floor(canvasHeight/this.dataMaze.rows)
      this.clearCanvas()
      for (let cell of this.dataMaze.cells) {
        this.drawCell(cell, colorCell, w, h)
      }
      if (this.solution) {
        this.drawSolution(w, h)
      }
      //  draw entry
      this.drawCell(this.dataMaze.entry, colorEntry, w, h)
      // draw exit
      this.drawCell(this.dataMaze.exit, colorExit, w, h)
    }
  }
}

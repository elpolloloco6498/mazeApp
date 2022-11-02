import { Component, OnInit, Output, EventEmitter} from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-mazeform',
  templateUrl: './mazeform.component.html',
  styleUrls: ['./mazeform.component.css']
})
export class MazeformComponent implements OnInit {
  mazeForm: FormGroup;
  @Output() data = new EventEmitter<any>();
  @Output() submitForm = new EventEmitter<any>();

  constructor(private fb: FormBuilder) { }

  updateFormData() {
    // make api call
    // send data to parent component
    this.data.emit({
      width: this.mazeForm.value.width,
      height: this.mazeForm.value.height,
      solution: this.mazeForm.value.solution
    });
  }

  emitSubmitEvent() {
    this.submitForm.emit(null);
  }

  ngOnInit(): void {
    this.mazeForm = this.fb.group({
      width: 10,
      height: 10,
      solution: false
    })
  }

}

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MazeformComponent } from './mazeform.component';

describe('MazeformComponent', () => {
  let component: MazeformComponent;
  let fixture: ComponentFixture<MazeformComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MazeformComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MazeformComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

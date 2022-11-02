import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MazedisplayComponent } from './mazedisplay.component';

describe('MazedisplayComponent', () => {
  let component: MazedisplayComponent;
  let fixture: ComponentFixture<MazedisplayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MazedisplayComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MazedisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

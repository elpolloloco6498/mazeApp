import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { MazeformComponent } from './components/mazeform/mazeform.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MazedisplayComponent } from './components/mazedisplay/mazedisplay.component';

@NgModule({
  declarations: [
    AppComponent,
    MazeformComponent,
    MazedisplayComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

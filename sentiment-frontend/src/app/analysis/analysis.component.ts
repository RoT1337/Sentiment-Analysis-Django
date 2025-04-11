import { Component } from '@angular/core';
import { NgForm, FormGroup, FormBuilder, Form } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-analysis',
  standalone: false,
  templateUrl: './analysis.component.html',
  styleUrl: './analysis.component.css'
})
export class AnalysisComponent {
  sentence: string = '';
  textForm: FormGroup;
  result: any;

  constructor(private http: HttpClient, private fb: FormBuilder) {
    this.textForm = this.fb.group({
      textInput: [''],
    });
  }

  onSubmit(event: Event): void {
    event.preventDefault();

    this.sentence = this.textForm.value.textInput;
    console.log("Checking sentence:", this.sentence);
    const post_data = {
      text: this.sentence,
    }
    console.log(post_data);

    this.http.post("http://127.0.0.1:8000/analysis", post_data).subscribe(
      data => {
        this.result = data;
      },
      error => {
        console.error('Error:', error);
      }
    );
  }
}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TasklistService } from './task-list.service';
import { ITaskList, ITasks, IAuthResponse } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends TasklistService{

  constructor(http:HttpClient){
    super(http);  
  }

  getTaskList():Promise<ITaskList[]>{
     return this.get('http://localhost:8000/api/tasklists/', {});
  }

  getTasks(tasklist: ITaskList): Promise<ITasks[]> {
    return this.get(`http://localhost:8000/api/tasklists/${tasklist.id}/tasks/`, {});
  }

  createTaskList(name:any):Promise<ITaskList>{
    return this.post('http://localhost:8000/api/tasklists/',{
      name:name
    });
  }

  updateTaskList(tasklist: ITaskList): Promise<ITaskList> {
    return this.put(`http://localhost:8000/api/tasklists/${tasklist.id}/`, {
      name: tasklist.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/tasklists/${id}/`, {});
  }

  auth(login:any,password:any):Promise<IAuthResponse>{
    return this.post('http://localhost:8000/api/login/',{
      username:login,
      password:password
    });
  }

  logout():Promise<any>{
    return this.post('http://localhost:8000/api/logout/',{

    });
  }
}

from rest_framework import serializers
from .models import Evaluation
from judges.serializers import JudgeListSerializer


class EvaluationListSerializer(serializers.ModelSerializer):
    judge = JudgeListSerializer(many=True, read_only=True)
    avg = serializers.SerializerMethodField(method_name="get_avg")
    class Meta:
        model= Evaluation
        fields = "__all__"

    def get_avg(self, obj:Evaluation):

        res = []
        teams = []
        judgeObjec = {}
        criteriaOfJudge = []
        for judge in obj.judge.all():
            judgeObjec = {"judge_id":judge.id,"judge_name": judge.name}
            for team in judge.grade:
                for criteria in team['grade']:
                    criteriaOfJudge.append({"criteria_id":criteria['criteria_id'], "criteria_name":criteria['criteria_name'], "criteria_weight":criteria['criteria_weight'], "criteria_score":criteria['grade']})                
                teams.append({**judgeObjec, "team_id":team['team_id'],"team_name":team['team_name'],"criteria":criteriaOfJudge, "note":{"judge_id":judge.id,"judge_name": judge.name,"note":team['note']}})
                criteriaOfJudge=[]
            res.append(teams)
            teams=[]
        avgWeight = []
        allRes = {}
        allRes2 = []
        responseObject = {"0":{'criteria':[]}, "judge":0}
        for i in [1,2]:
            for judge in res:
                for team in judge:
                    if team['team_id'] in responseObject.keys():
                        responseObject = {**responseObject,team['team_id']:{**responseObject[team['team_id']], "team_id":team['team_id'], "team_name":team['team_name']}}
                        if(i == 1):
                            
                            responseObject[team['team_id']]['notes'].append(team['note'])
                    else:
                        responseObject = {**responseObject, team['team_id']:{ "team_id":team['team_id'], "team_name":team['team_name'], "notes":[team['note']]}}
                        

                    for index,criteria in enumerate(team['criteria']):
                        if "criteria" in responseObject[team['team_id']].keys():
                            if {**criteria, "criteria_score":0, "avg":0, "avg_weight":0} in [{**item, "criteria_score":0, "avg":0, "avg_weight":0} for item in responseObject[team['team_id']]['criteria']]:

                                if(i == 1):
                                    responseObject[team['team_id']]['criteria'][index]['criteria_score'].append(criteria['criteria_score'])
                                responseObject[team['team_id']]['criteria'][index]['avg']= round(((sum(responseObject[team['team_id']]['criteria'][index]['criteria_score'])/len(responseObject[team['team_id']]['criteria'][index]['criteria_score']))*10),3)
                                responseObject[team['team_id']]['criteria'][index]['avg_weight']= round(((responseObject[team['team_id']]['criteria'][index]['avg']*responseObject[team['team_id']]['criteria'][index]['criteria_weight'])/100),3)
                                avgWeight.append(responseObject[team['team_id']]['criteria'][index]['avg'])
                                if criteria['criteria_id'] in allRes.keys():

                                    allRes[criteria['criteria_id']]['avg'].append(responseObject[team['team_id']]['criteria'][index]['avg'])
                                    allRes[criteria['criteria_id']]['avg_weight'].append(responseObject[team['team_id']]['criteria'][index]['avg_weight'])
                                    allRes[criteria['criteria_id']]['avgT'] = round((sum(allRes[criteria['criteria_id']]['avg'])/len(allRes[criteria['criteria_id']]['avg'])),2)
                                    allRes[criteria['criteria_id']]['avg_weightT'] = round((sum(allRes[criteria['criteria_id']]['avg_weight'])/len(allRes[criteria['criteria_id']]['avg_weight'])),2)

                                    allRes2.append({"criteria_id": criteria['criteria_id'], "criteria_name":criteria['criteria_name'], "criteria_weight":criteria['criteria_weight'], "avg":allRes[criteria['criteria_id']]['avgT'], "avg_weight": allRes[criteria['criteria_id']]['avg_weightT']})
                                else:
                                    allRes = { **allRes, criteria['criteria_id']:{"avg":[responseObject[team['team_id']]['criteria'][index]['avg']], "avg_weight":[responseObject[team['team_id']]['criteria'][index]['avg_weight']]}}
                                    allRes[criteria['criteria_id']]['avgT'] = round((sum(allRes[criteria['criteria_id']]['avg'])/len(allRes[criteria['criteria_id']]['avg'])),2)
                                    allRes[criteria['criteria_id']]['avg_weightT'] = round((sum(allRes[criteria['criteria_id']]['avg_weight'])/len(allRes[criteria['criteria_id']]['avg_weight'])),2)

                                    allRes2.append({"criteria_id": criteria['criteria_id'], "criteria_name":criteria['criteria_name'], "criteria_weight":criteria['criteria_weight'], "avg":allRes[criteria['criteria_id']]['avgT'], "avg_weight": allRes[criteria['criteria_id']]['avg_weightT']})


                            else:
                                

                                responseObject[team['team_id']]['criteria'].append({**criteria, "criteria_score":[criteria['criteria_score']]}) 

                        else:
                            responseObject[team['team_id']]['criteria'] = [{**criteria, "criteria_score":[criteria['criteria_score']]}]


                    responseObject['t_criteria'] = len(team['criteria'])
                    if(len(avgWeight)>0):
                        responseObject[team['team_id']]['total'] = round((sum(avgWeight)/len(avgWeight)),2)
                        avgWeight = []
                responseObject['judge']=len(res)
                responseObject['0']['total'] = round((sum([total['avg'] for total in allRes2[-responseObject['t_criteria']:]])/responseObject['t_criteria']),2)
                responseObject['0']['criteria'] = allRes2[-responseObject['t_criteria']:]
        return responseObject
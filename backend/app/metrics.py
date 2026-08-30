from dataclasses import dataclass, field
@dataclass
class MetricsStore:
    analyzed:int=0
    feedback_count:int=0
    accepted_count:int=0
    latencies_ms:list[float]=field(default_factory=list)
    def record_analysis(self,latency_ms): self.analyzed+=1; self.latencies_ms.append(latency_ms)
    def record_feedback(self,accepted):
        self.feedback_count+=1
        if accepted:self.accepted_count+=1
    def snapshot(self):
        avg=sum(self.latencies_ms)/len(self.latencies_ms) if self.latencies_ms else 0.0
        acceptance=self.accepted_count/self.feedback_count if self.feedback_count else None
        return {"tickets_analyzed":self.analyzed,"average_latency_ms":round(avg,2),"feedback_count":self.feedback_count,"acceptance_rate":round(acceptance,3) if acceptance is not None else None}
metrics_store=MetricsStore()

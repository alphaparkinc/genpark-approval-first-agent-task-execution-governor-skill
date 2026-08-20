from client import ApprovalFirstAgentTaskExecutionGovernorClient

def main():
    client = ApprovalFirstAgentTaskExecutionGovernorClient()
    action = {"type": "bulk_email_campaign", "target_users": 5200, "campaign": "renewal_Q3_2026"}
    res = client.evaluate_action(action, risk_level="HIGH")
    print(f"Approval Required: {res['approval_required']}")
    print(f"Risk Assessment: {res['risk_assessment']}")
    print(f"Rollback Plan: {res['rollback_plan']}")
    print("Safe Execution Plan:")
    for step in res["safe_execution_plan"]:
        print(f"  {step}")

if __name__ == "__main__":
    main()

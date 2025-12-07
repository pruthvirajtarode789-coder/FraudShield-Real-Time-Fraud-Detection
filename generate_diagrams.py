"""
Generate comprehensive UML and system architecture diagrams for FraudShield project.
Uses Graphviz to create professional PNG diagrams.
"""

import os
import subprocess
import sys
from pathlib import Path

# Ensure graphviz is installed
try:
    import graphviz
except ImportError:
    print("Installing graphviz package...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "graphviz"])
    import graphviz

# Create diagrams directory
diagrams_dir = Path(__file__).parent / "diagrams"
diagrams_dir.mkdir(exist_ok=True)

def create_usecase_diagram():
    """Create Use Case Diagram showing actors and their interactions."""
    dot = graphviz.Digraph(name='01_UseCase_Diagram', format='png', directory=str(diagrams_dir))
    dot.attr(rankdir='LR', bgcolor='#f8f9fa', dpi='300')
    dot.attr('node', shape='ellipse', style='filled', fillcolor='#e0e7ff', fontname='Arial', fontsize='10')
    
    # Actors
    dot.node('user', 'User', shape='box', fillcolor='#6366f1', fontcolor='white', fontsize='11', style='filled')
    dot.node('data_scientist', 'Data Scientist', shape='box', fillcolor='#6366f1', fontcolor='white', fontsize='11', style='filled')
    dot.node('admin', 'Admin', shape='box', fillcolor='#6366f1', fontcolor='white', fontsize='11', style='filled')
    
    # Use Cases
    dot.node('uc1', 'Detect Fraud', shape='ellipse', fillcolor='#dbeafe')
    dot.node('uc2', 'Input Transaction', shape='ellipse', fillcolor='#dbeafe')
    dot.node('uc3', 'View Analytics', shape='ellipse', fillcolor='#dbeafe')
    dot.node('uc4', 'Export Report', shape='ellipse', fillcolor='#dbeafe')
    dot.node('uc5', 'Train Model', shape='ellipse', fillcolor='#dbeafe')
    dot.node('uc6', 'Manage System', shape='ellipse', fillcolor='#dbeafe')
    
    # Relationships
    dot.edge('user', 'uc1')
    dot.edge('user', 'uc2')
    dot.edge('user', 'uc3')
    dot.edge('user', 'uc4')
    dot.edge('data_scientist', 'uc5')
    dot.edge('admin', 'uc6')
    
    dot.render()
    print("✓ Use Case Diagram created")

def create_sequence_diagram():
    """Create Sequence Diagram showing interaction flow."""
    dot = graphviz.Digraph(name='02_Sequence_Diagram', format='png', directory=str(diagrams_dir))
    dot.attr(rankdir='LR', bgcolor='#f8f9fa', dpi='300')
    dot.attr('node', shape='box', style='filled', fillcolor='#dbeafe', fontname='Arial', fontsize='9')
    
    # Actors and Components
    actors = ['User', 'Streamlit\nApp', 'FastAPI\nServer', 'ML\nModel', 'Database']
    for i, actor in enumerate(actors):
        dot.node(f'actor{i}', actor, fillcolor='#6366f1' if i in [1, 2, 3] else '#10b981', 
                fontcolor='white', fontsize='10', style='filled')
    
    # Sequence flow
    dot.edge('actor0', 'actor1', label='1. Input Transaction', fontsize='8')
    dot.edge('actor1', 'actor2', label='2. API Request', fontsize='8')
    dot.edge('actor2', 'actor3', label='3. Predict', fontsize='8')
    dot.edge('actor3', 'actor2', label='4. Result', fontsize='8')
    dot.edge('actor2', 'actor4', label='5. Store Result', fontsize='8')
    dot.edge('actor2', 'actor1', label='6. Response', fontsize='8')
    dot.edge('actor1', 'actor0', label='7. Display Output', fontsize='8')
    
    dot.render()
    print("✓ Sequence Diagram created")

def create_architecture_diagram():
    """Create System Architecture Diagram."""
    dot = graphviz.Digraph(name='03_Architecture_Diagram', format='png', directory=str(diagrams_dir))
    dot.attr(rankdir='TB', bgcolor='#f8f9fa', dpi='300')
    dot.attr('node', shape='box', style='filled', fontname='Arial', fontsize='10')
    
    # Layers
    dot.node('pres', 'Presentation Layer\n(Streamlit UI)', fillcolor='#dbeafe', style='filled')
    dot.node('app', 'Application Layer\n(FastAPI Server)', fillcolor='#c7d2fe', style='filled')
    dot.node('logic', 'Business Logic Layer\n(ML Model)', fillcolor='#a5b4fc', style='filled')
    dot.node('data', 'Data Layer\n(Models & Data)', fillcolor='#818cf8', fontcolor='white', style='filled')
    
    dot.edge('pres', 'app', label='HTTP Requests')
    dot.edge('app', 'logic', label='Predictions')
    dot.edge('logic', 'data', label='Features')
    
    dot.render()
    print("✓ Architecture Diagram created")

def create_dataflow_diagram():
    """Create Data Flow Diagram."""
    dot = graphviz.Digraph(name='04_DataFlow_Diagram', format='png', directory=str(diagrams_dir))
    dot.attr(rankdir='LR', bgcolor='#f8f9fa', dpi='300')
    dot.attr('node', shape='ellipse', style='filled', fontname='Arial', fontsize='9')
    
    # Processes and data stores
    dot.node('raw_data', 'Raw Transaction\nData', fillcolor='#fed7aa', shape='box')
    dot.node('preprocess', 'Data\nPreprocessing', fillcolor='#fbbf24', shape='ellipse')
    dot.node('train', 'Model\nTraining', fillcolor='#f59e0b', shape='ellipse')
    dot.node('model', 'Trained\nModel', fillcolor='#10b981', shape='box')
    dot.node('api', 'API\nEndpoint', fillcolor='#6366f1', fontcolor='white', shape='ellipse')
    dot.node('input', 'New\nTransaction', fillcolor='#fed7aa', shape='box')
    dot.node('predict', 'Prediction\nEngine', fillcolor='#a78bfa', shape='ellipse')
    dot.node('output', 'Fraud Score &\nRisk Level', fillcolor='#10b981', shape='box')
    
    dot.edge('raw_data', 'preprocess')
    dot.edge('preprocess', 'train')
    dot.edge('train', 'model')
    dot.edge('model', 'api')
    dot.edge('input', 'api')
    dot.edge('api', 'predict')
    dot.edge('predict', 'output')
    
    dot.render()
    print("✓ Data Flow Diagram created")

def create_component_diagram():
    """Create Component Diagram."""
    dot = graphviz.Digraph(name='05_Component_Diagram', format='png', directory=str(diagrams_dir))
    dot.attr(rankdir='TB', bgcolor='#f8f9fa', dpi='300')
    dot.attr('node', shape='box', style='filled', fontname='Arial', fontsize='10')
    
    # Components
    components = [
        ('ui', 'Streamlit UI', '#dbeafe'),
        ('api', 'FastAPI Server', '#c7d2fe'),
        ('model', 'ML Model\n(Logistic Regression)', '#a5b4fc'),
        ('preprocess', 'Data Preprocessor', '#fbbf24'),
        ('storage', 'Model Storage', '#10b981'),
    ]
    
    for comp_id, comp_name, color in components:
        dot.node(comp_id, comp_name, fillcolor=color, style='filled')
    
    dot.edge('ui', 'api', label='calls')
    dot.edge('api', 'model', label='uses')
    dot.edge('model', 'preprocess', label='processes')
    dot.edge('preprocess', 'storage', label='loads')
    
    dot.render()
    print("✓ Component Diagram created")

def create_deployment_diagram():
    """Create Deployment Diagram."""
    dot = graphviz.Digraph(name='06_Deployment_Diagram', format='png', directory=str(diagrams_dir))
    dot.attr(rankdir='LR', bgcolor='#f8f9fa', dpi='300')
    dot.attr('node', shape='box', style='filled', fontname='Arial', fontsize='10')
    
    # Environments
    dot.node('dev', 'Development\nEnvironment\n(Local)', fillcolor='#dbeafe', style='filled')
    dot.node('docker', 'Docker\nContainer', fillcolor='#a78bfa', fontcolor='white', style='filled')
    dot.node('prod', 'Production\nEnvironment\n(Server)', fillcolor='#10b981', fontcolor='white', style='filled')
    dot.node('client', 'Client\nBrowser', fillcolor='#fed7aa', style='filled')
    
    dot.edge('dev', 'docker', label='Build')
    dot.edge('docker', 'prod', label='Deploy')
    dot.edge('prod', 'client', label='Serve UI')
    
    dot.render()
    print("✓ Deployment Diagram created")

def create_activity_diagram():
    """Create Activity Diagram showing process workflow."""
    dot = graphviz.Digraph(name='07_Activity_Diagram', format='png', directory=str(diagrams_dir))
    dot.attr(rankdir='TB', bgcolor='#f8f9fa', dpi='300')
    dot.attr('node', shape='ellipse', style='filled', fontname='Arial', fontsize='9')
    
    # Activities
    dot.node('start', 'Start', fillcolor='#10b981', fontcolor='white', shape='circle', width='0.5')
    dot.node('open', 'Open Application', fillcolor='#dbeafe')
    dot.node('input', 'Input Transaction\nData', fillcolor='#dbeafe')
    dot.node('validate', 'Validate Input', fillcolor='#fbbf24')
    dot.node('process', 'Process with\nML Model', fillcolor='#a78bfa', fontcolor='white')
    dot.node('display', 'Display Results &\nAnalytics', fillcolor='#dbeafe')
    dot.node('export', 'Export Report\n(Optional)', fillcolor='#dbeafe')
    dot.node('end', 'End', fillcolor='#ef4444', fontcolor='white', shape='circle', width='0.5')
    
    dot.edge('start', 'open')
    dot.edge('open', 'input')
    dot.edge('input', 'validate')
    dot.edge('validate', 'process')
    dot.edge('process', 'display')
    dot.edge('display', 'export')
    dot.edge('export', 'end')
    
    dot.render()
    print("✓ Activity Diagram created")

def create_class_diagram():
    """Create Class Diagram showing OOP structure."""
    dot = graphviz.Digraph(name='08_Class_Diagram', format='png', directory=str(diagrams_dir))
    dot.attr(rankdir='TB', bgcolor='#f8f9fa', dpi='300')
    dot.attr('node', shape='record', style='filled', fontname='Arial', fontsize='8')
    
    # Classes
    dot.node('transaction', '''
    {
      TransactionData |
      - transaction_id: str \\l
      - amount: float \\l
      - merchant: str \\l
      - category: str \\l
      + validate(): bool \\l
      + preprocess(): dict \\l
    }
    ''', fillcolor='#dbeafe')
    
    dot.node('model', '''
    {
      MLModel |
      - model_path: str \\l
      - columns: list \\l
      - scaler: StandardScaler \\l
      + load_model(): void \\l
      + predict(data): float \\l
      + get_probability(): float \\l
    }
    ''', fillcolor='#c7d2fe')
    
    dot.node('detector', '''
    {
      FraudDetector |
      - model: MLModel \\l
      - preprocessor: Preprocessor \\l
      + detect_fraud(transaction): dict \\l
      + get_risk_score(): float \\l
      + generate_report(): dict \\l
    }
    ''', fillcolor='#a5b4fc', fontcolor='white')
    
    dot.node('ui', '''
    {
      StreamlitUI |
      - api_url: str \\l
      - session_state: dict \\l
      + render_dashboard(): void \\l
      + handle_input(): dict \\l
      + display_results(): void \\l
    }
    ''', fillcolor='#fbbf24')
    
    # Relationships
    dot.edge('ui', 'detector', label='uses')
    dot.edge('detector', 'model', label='uses')
    dot.edge('detector', 'transaction', label='processes')
    
    dot.render()
    print("✓ Class Diagram created")

def main():
    """Generate all diagrams."""
    print("\n" + "="*60)
    print("FraudShield System Diagram Generation")
    print("="*60 + "\n")
    
    try:
        create_usecase_diagram()
        create_sequence_diagram()
        create_architecture_diagram()
        create_dataflow_diagram()
        create_component_diagram()
        create_deployment_diagram()
        create_activity_diagram()
        create_class_diagram()
        
        print("\n" + "="*60)
        print("✓ All diagrams generated successfully!")
        print(f"✓ Location: {diagrams_dir}")
        print("="*60 + "\n")
        
        # List generated files
        png_files = list(diagrams_dir.glob("*.png"))
        print("Generated files:")
        for f in sorted(png_files):
            print(f"  • {f.name}")
        
    except Exception as e:
        print(f"\n✗ Error generating diagrams: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
